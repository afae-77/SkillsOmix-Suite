# Load libraries
library(DESeq2)
library(tidyverse)

# Define function
run_deseq2 <- function(count_path, metadata_path, output_path) {
  counts <- read.csv(count_path, row.names=1)
  metadata <- read.csv(metadata_path)
  
  dds <- DESeqDataSetFromMatrix(countData = counts,
                                colData = metadata,
                                design = ~ condition)
  dds <- DESeq(dds)
  res <- results(dds)
  
  write.csv(as.data.frame(res), file.path(output_path, "deseq2_results.csv"))
}
