# SkillsOmix-Suite
Open-source platform for transcriptome and genome analysis with statistical and bioinformatics pipelines.

**SkillsOmix-Suite** is a free, open-source platform for transcriptome and genome analysis. It empowers researchers and students to perform comprehensive bioinformatics and statistical assessments on sequencing data through an interactive, bilingual web-based interface.

Inspired by the modularity and community-driven philosophy of Linux, SkillsOmix-Suite is designed to be constantly updated, extensible, and accessible to all.

Any researcher can add and modify the tools and databases, suiting their sample data and organisms.

Features

- 🔬 **Transcriptome Analysis**: DESeq2, edgeR, limma, GSEA, GO/KEGG enrichment
- 🧬 **Genome Analysis**: Variant calling (GATK, bcftools), annotation (SnpEff), GWAS
- 🌱 **Microbiome Profiling**: 16S/shotgun pipelines, functional profiling via PICRUSt2/HUMAnN
- 📊 **Interactive Visualization**: Volcano plots, PCA, heatmaps, correlation matrices
- 🌐 **Bilingual Interface**: English and Arabic support for broader accessibility
- 📦 **Modular Architecture**: Easily add or modify pipelines and tools
- 🧠 **AI-Assisted Annotation** *(coming soon)*: NLP-based biological interpretation
- 🖥️ **Web-Based & Local Deployment**: Use online or via Docker/Conda offline

## 🛠️ Installation

SkillsOmix-Suite is built as a web-based application using Python, R, and optionally React or Streamlit.

### 🔹 Requirements
- Python ≥ 3.9
- R ≥ 4.2
- Conda or Docker (recommended for reproducibility)

### 🔹 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/afae-77/SkillsOmix-Suite.git
cd SkillsOmix-Suite

# Create environment
conda env create -f env/environment.yml
conda activate skillsomix

# Run backend API
python backend/api/run_pipeline.py

# (Optional) Launch frontend
streamlit run frontend/pages/upload_interface.py

Contribution Guidelines
We welcome contributions from researchers, developers, and educators worldwide.

🔹 How to Contribute
Fork the repository

Create a new branch (git checkout -b feature-name)

Add your module or fix

Submit a pull request with a clear description

What You Can Contribute
New analysis pipelines (e.g., single-cell RNA-seq, metagenomics)

UI/UX improvements

Documentation in English or Arabic

Bug fixes and performance enhancements

See docs/architecture.md for design principles and module structure.

Citation Format
SkillsOmix-Suite is currently under active development and has not yet been formally published. If you use it in your research, please cite it as follows:

@misc{SkillsOmixSuite2025,
  author       = {Ahmed F. and contributors},
  title        = {SkillsOmix-Suite: An open-source platform for transcriptome and genome analysis},
  year         = {2025},
  howpublished = {\url{https://github.com/afae-77/SkillsOmix-Suite}},
  note         = {Accessed: [Insert date]}
}
Once the project is published in a peer-reviewed journal or preprint server, we will update this section with the official citation.

Acknowledgments
SkillsOmix-Suite is built with the belief that advanced scientific tools should be free, transparent, and accessible to all. We thank the open-source community and all contributors who share this vision.

# SkillsOmix-Suite

**SkillsOmix-Suite** is a free, open-source platform for transcriptome and genome analysis. It integrates statistical and bioinformatics pipelines with a modular, bilingual interface.

## 🚀 Features
- RNA-seq analysis (DESeq2, edgeR, GSEA)
- Variant calling and annotation
- Microbiome profiling
- Interactive plots and dashboards
- English/Arabic interface
- Docker-ready and Linux-compatible

## 🧪 Getting Started
1. Clone the repo
2. Install dependencies from `env/environment.yml`
3. Run the backend API
4. Upload count and metadata files via frontend

## 🤝 Contributing
We welcome pull requests, feature suggestions, and community modules. See `docs/architecture.md` for guidelines.

## 📜 License
GNU GPLv3








