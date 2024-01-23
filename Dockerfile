FROM python:3.8
RUN pip install pandas scikit-learn==1.2.2 streamlit joblib
COPY src/app.py /app/
COPY model/cardiopatia_model.pkl /app/model/cardiopatia_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]