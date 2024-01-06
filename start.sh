#!/bin/sh

source venv/bin/activate

if [ ! -d "logs" ]; then
    mkdir logs
fi

echo "🐍  Starting app ..."
nohup streamlit run app.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    --server.headless true \
    &> logs/streamlit.log 2>&1 &
echo "🏃🏻  App started!"

tail -f logs/streamlit.log

