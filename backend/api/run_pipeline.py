from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/run_deseq2', methods=['POST'])
def run_deseq2():
    count_file = request.files['counts']
    metadata_file = request.files['metadata']
    
    os.makedirs("temp", exist_ok=True)
    count_path = os.path.join("temp", count_file.filename)
    metadata_path = os.path.join("temp", metadata_file.filename)
    
    count_file.save(count_path)
    metadata_file.save(metadata_path)
    
    subprocess.run(["Rscript", "backend/pipelines/rnaseq_deseq2.R", count_path, metadata_path, "results"])
    
    return {"status": "completed", "results": "results/deseq2_results.csv"}
