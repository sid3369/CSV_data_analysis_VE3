import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile
import matplotlib.pyplot as plt
import seaborn as sns
from django.conf import settings
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.conf import settings
import matplotlib
matplotlib.use('Agg')  

def get_base64_image(plt):
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            file_path = uploaded_file.file.path

            df = pd.read_csv(file_path)

            columns_to_drop = [
                'Urban Population % of Total Population',
                '% Increase in Urban Population',
                'Rural Population',
                'Rural Population % of Total Population',
                '% Increase in Rural Population'
            ]
            df.drop(columns=columns_to_drop, inplace=True)

            data_preview = df.head().to_html()
            data_size = df.shape
            missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()
            summary_statistics = df.describe().to_html()
            mean_values = df.mean(numeric_only=True).to_frame(name='Mean').to_html()
            median_values = df.median(numeric_only=True).to_frame(name='Median').to_html()
            std_values = df.std(numeric_only=True).to_frame(name='Standard Deviation').to_html()
            columns = pd.DataFrame(df.columns, columns=['Column Names']).to_html(index=False)
            dropped_columns = pd.DataFrame(columns_to_drop, columns=['Dropped Columns']).to_html(index=False)

            visualizations = []

            plt.figure(figsize=(13, 13))
            sns.lineplot(data=df, x='Year', y='Population')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Population Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.lineplot(data=df, x='Year', y='Birth Rate')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Birth Rate Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.lineplot(data=df, x='Year', y='Life Expectancy')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Life Expectancy Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.lineplot(data=df, x='Year', y='Infant Mortality Rate')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Infant Mortality Rate Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.lineplot(data=df, x='Year', y='Fertility Rate')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Fertility Rate Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.lineplot(data=df, x='Year', y='Net Migration Rate')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Net Migration Rate Over Years', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.histplot(df['Population'], bins=20, kde=True)
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Population Distribution', 'image': base64_image})
            plt.close()

            plt.figure()
            sns.boxplot(data=df, y='Life Expectancy')
            base64_image = get_base64_image(plt)
            visualizations.append({'title': 'Life Expectancy Distribution', 'image': base64_image})
            plt.close()

            context = {
                'form': form,
                'data_preview': data_preview,
                'data_size': data_size,
                'missing_values': missing_values,
                'summary_statistics': summary_statistics,
                'mean_values': mean_values,
                'median_values': median_values,
                'std_values': std_values,
                'columns': columns,
                'dropped_columns': dropped_columns,
                'visualizations': visualizations,
            }
            return render(request, 'upload.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
