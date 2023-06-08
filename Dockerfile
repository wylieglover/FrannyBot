FROM python
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "/bot/bot.py"]