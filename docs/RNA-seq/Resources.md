## 1. Reference genomes

On [Biowulf](https://hpc.nih.gov/), RENEE comes bundled with the following pre-built [GENCODE](https://www.gencodegenes.org/)<sup>1</sup> reference genomes:

As of RENEE v2.6.0, all hg19 and hg38 indices were built using the
[NCI Genomic Data Commons reference fasta](https://gdc.cancer.gov/about-data/gdc-data-processing/gdc-reference-files),
which contains the primary genome from Encode plus virus and decoy sequences.
The hg38 fasta files were downloaded from the GDC with virus and decoy sequences already added,
while these sequences were manually added to the hg19 fasta from Encode.
See details here: <https://github.com/CCBR/build-renee-refs>

| **Genome**    | **Species**                                      | **Annotation Version**                                                                                                                                                                                                                    | **Notes**                                |
| ------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| hg38_48       | _Homo sapiens_ (human)                           | [Gencode Release 48](https://www.gencodegenes.org/human/release_48.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 05/2025 |
| hg38_45       | _Homo sapiens_ (human)                           | [Gencode Release 45](https://www.gencodegenes.org/human/release_45.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 03/2023 |
| hg38_41       | _Homo sapiens_ (human)                           | [Gencode Release 41](https://www.gencodegenes.org/human/release_41.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 07/2022 |
| hg38_38       | _Homo sapiens_ (human)                           | [Gencode Release 38](https://www.gencodegenes.org/human/release_38.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 05/2021 |
| hg38_36       | _Homo sapiens_ (human)                           | [Gencode Release 36](https://www.gencodegenes.org/human/release_36.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 05/2020 |
| hg38_34       | _Homo sapiens_ (human)                           | [Gencode Release 34](https://www.gencodegenes.org/human/release_34.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 04/2020 |
| hg38_30       | _Homo sapiens_ (human)                           | [Gencode Release 30](https://www.gencodegenes.org/human/release_30.html)                                                                                                                                                                  | GRCh38, Annotation Release date: 11/2018 |
| hg19_36       | _Homo sapiens_ (human)                           | [Gencode Release 36-lift-37](https://www.gencodegenes.org/human/release_36lift37.html)                                                                                                                                                    | GRCh37                                   |
| hg19_19       | _Homo sapiens_ (human)                           | [Gencode Release 19](https://www.gencodegenes.org/human/release_19.html)                                                                                                                                                                  | GRCh37, Annotation Release date: 07/2013 |
| mm39_M37      | _Mus musculus_ (mouse)                           | [Gencode Release M37](https://www.gencodegenes.org/mouse/release_M36.html)                                                                                                                                                                | GRCm39, Annotation Release date: 05/2025 |
| mm39_M36      | _Mus musculus_ (mouse)                           | [Gencode Release M36](https://www.gencodegenes.org/mouse/release_M36.html)                                                                                                                                                                | GRCm39, Annotation Release date: 10/2024 |
| mm10_M25      | _Mus musculus_ (mouse)                           | [Gencode Release M25](https://www.gencodegenes.org/mouse/release_M25.html)                                                                                                                                                                | GRCm38, Annotation Release date: 04/2020 |
| mm10_M23      | _Mus musculus_ (mouse)                           | [Gencode Release M23](https://www.gencodegenes.org/mouse/release_M23.html)                                                                                                                                                                | GRCm38, Annotation Release date: 09/2019 |
| mm10_M21      | _Mus musculus_ (mouse)                           | [Gencode Release M21](https://www.gencodegenes.org/mouse/release_M21.html)                                                                                                                                                                | GRCm38, Annotation Release date: 04/2019 |
| mCalJac1_2021 | _Callithrix jacchus_ (white-tufted-ear marmoset) | [Genome assembly mCalJa1.2.pat.X](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_011100555.1/)                                                                                                                                          | Annotation release date: 04/2021         |
| mmul10_108    | _Macaca mulatta_ (rhesus macaque)                | Ensemble 108: [fasta](https://ftp.ensembl.org/pub/release-108/fasta/macaca_mulatta/dna/Macaca_mulatta.Mmul_10.dna_rm.toplevel.fa.gz); [gtf](https://ftp.ensembl.org/pub/release-108/gtf/macaca_mulatta/Macaca_mulatta.Mmul_10.108.gtf.gz) | Annotation release date: 09/2022         |

You can run `renee run --help` to view the most up-to-date list of genome annotations available in your installation of RENEE.

> **Note:** Newer annotations versions may be added upon request and may be already available. Please contact [Vishal Koparde](mailto:vishal.koparde@nih.gov) for details.

However, building new reference genomes is easy!

If you do not have access to Biowulf or you are looking for a reference genome and/or annotation **_that is currently not available_**, it can be built with RENEE's build sub-command. Given a genomic FASTA file (ref.fa) and a GTF file (genes.gtf), `renee build` will create all of the required reference files to run the RENEE pipeline. Once the build pipeline completes, you can supply the newly generated reference.json to the `--genome` of `renee run`. For more information, please see the help page for the run and build sub commands.

## 2. Tools and versions

> _Raw data > Adapter Trimming > Alignment > Quantification (genes and isoforms, gene-fusions)_

| **Tool**                 |                                              **Version**                                              | **Docker**                                                                                                    | **Notes**                                                                                                                                       |
| ------------------------ | :---------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| FastQC<sup>2</sup>       |                                                0.11.9                                                 | [nciccbr/ccbr_fastqc_0.11.9](https://hub.docker.com/repository/docker/nciccbr/ccbr_fastqc_0.11.9)             | **Quality-control step** to assess sequencing quality, run before and after adapter trimming                                                    |
| Cutadapt<sup>3</sup>     |                                                 1.18                                                  | [nciccbr/ccbr_cutadapt_1.18](https://hub.docker.com/repository/docker/nciccbr/ccbr_cutadapt_1.18)             | **Data processing step** to remove adapter sequences and perform quality trimming                                                               |
| Kraken<sup>4</sup>       |                                                 2.1.1                                                 | [nciccbr/ccbr_kraken_v2.1.1](https://hub.docker.com/repository/docker/nciccbr/ccbr_kraken_v2.1.1)             | **Quality-control step** to assess microbial taxonomic composition                                                                              |
| KronaTools<sup>5</sup>   |                                                 2.7.1                                                 | [nciccbr/ccbr_kraken_v2.1.1](https://hub.docker.com/repository/docker/nciccbr/ccbr_kraken_v2.1.1)             | **Quality-control step** to visualize kraken output                                                                                             |
| FastQ Screen<sup>6</sup> |                                                0.13.0                                                 | [nciccbr/ccbr_fastq_screen_0.13.0](https://hub.docker.com/repository/docker/nciccbr/ccbr_fastq_screen_0.13.0) | **Quality-control step** to assess contamination; additional dependencies: `bowtie2/2.3.4`, `perl/5.24.3`                                       |
| STAR<sup>7</sup>         |                                                2.7.6a                                                 | [nciccbr/ccbr_arriba_2.0.0](https://hub.docker.com/repository/docker/nciccbr/ccbr_arriba_2.0.0)               | **Data processing step** to align reads against reference genome (using its two-pass mode)                                                      |
| bbtools<sup>8</sup>      |                                                 38.87                                                 | [nciccbr/ccbr_bbtools_38.87](https://hub.docker.com/repository/docker/nciccbr/ccbr_bbtools_38.87)             | **Quality-control step** to calculate insert_size of assembled reads pairs with `bbmerge`                                                       |
| QualiMap<sup>9</sup>     |                                                 2.2.1                                                 | [nciccbr/ccbr_qualimap](https://hub.docker.com/repository/docker/nciccbr/ccbr_qualimap)                       | **Quality-control step** to assess various alignment metrics                                                                                    |
| Picard<sup>10</sup>      |                                                2.18.20                                                | [nciccbr/ccbr_picard](https://hub.docker.com/repository/docker/nciccbr/ccbr_picard)                           | **Quality-control step** to run `MarkDuplicates`, `CollectRnaSeqMetrics` and `AddOrReplaceReadGroups`                                           |
| Preseq<sup>11</sup>      |                                                 2.0.3                                                 | [nciccbr/ccbr_preseq](https://hub.docker.com/repository/docker/nciccbr/ccbr_preseq)                           | **Quality-control step** to estimate library complexity                                                                                         |
| SAMtools<sup>12</sup>    |                                                  1.7                                                  | [nciccbr/ccbr_arriba_2.0.0](https://hub.docker.com/repository/docker/nciccbr/ccbr_arriba_2.0.0)               | **Quality-control step** to run `flagstat` to calculate alignment statistics                                                                    |
| bam2strandedbw           | [custom](https://github.com/CCBR/Pipeliner/blob/master/Results-template/Scripts/bam2strandedbw.pe.sh) | [nciccbr/ccbr_bam2strandedbw](https://hub.docker.com/repository/docker/nciccbr/ccbr_bam2strandedbw)           | **Summarization step** to convert STAR aligned PE bam file into forward and reverse strand bigwigs suitable for a genomic track viewer like IGV |
| RSeQC<sup>13</sup>       |                                                 4.0.0                                                 | [nciccbr/ccbr_rseqc_4.0.0](https://hub.docker.com/repository/docker/nciccbr/ccbr_rseqc_4.0.0)                 | **Quality-control step** to infer stranded-ness and read distributions over specific genomic features                                           |
| RSEM<sup>14</sup>        |                                                 1.3.3                                                 | [nciccbr/ccbr_rsem_1.3.3](https://hub.docker.com/repository/docker/nciccbr/ccbr_rsem_1.3.3)                   | **Data processing step** to quantify gene and isoform counts                                                                                    |
| Arriba<sup>15<sup>       |                                                 2.0.0                                                 | [nciccbr/ccbr_arriba_2.0.0](https://hub.docker.com/repository/docker/nciccbr/ccbr_arriba_2.0.0)               | **Data processing step** to quantify gene-fusions                                                                                               |
| RNA Report               |                                 [custom](https://github.com/CCBR/rNA)                                 | [nciccbr/ccbr_rna](https://hub.docker.com/repository/docker/nciccbr/ccbr_rna)                                 | **Summarization step** to identify outliers and assess technical sources of variation                                                           |
| MultiQC<sup>16</sup>     |                                                 1.12                                                  | [skchronicles/multiqc](https://hub.docker.com/repository/docker/skchronicles/multiqc/)                        | **Reporting step** to aggregate sample statistics and quality-control information across all sample                                             |

## 3. Acknowledgements

### 3.1 Biowulf

If you [utilized NIH's Biowulf cluster](https://hpc.nih.gov/Research/) to run RENEE, _please do not forget to provide an acknowlegement_!

> The continued growth and support of NIH's Biowulf cluster is dependent upon its demonstrable value to the NIH Intramural Research Program. If you publish research that involved significant use of Biowulf, please cite the cluster.

**Suggested citation text:**

```
This work utilized the computational resources of the NIH HPC Biowulf cluster. (http://hpc.nih.gov)
```

## 4. References

<sup>**1.** Harrow, J., et al., GENCODE: the reference human genome annotation for The ENCODE Project. Genome Res, 2012. 22(9): p. 1760-74.</sup>  
<sup>**2.** Andrews, S. (2010). FastQC: a quality control tool for high throughput sequence data.</sup>  
<sup>**3.** Martin, M. (2011). "Cutadapt removes adapter sequences from high-throughput sequencing reads." EMBnet 17(1): 10-12.</sup>  
<sup>**4.** Wood, D. E. and S. L. Salzberg (2014). "Kraken: ultrafast metagenomic sequence classification using exact alignments." Genome Biol 15(3): R46.</sup>  
<sup>**5.** Ondov, B. D., et al. (2011). "Interactive metagenomic visualization in a Web browser." BMC Bioinformatics 12(1): 385.</sup>  
<sup>**6.** Wingett, S. and S. Andrews (2018). "FastQ Screen: A tool for multi-genome mapping and quality control." F1000Research 7(2): 1338.</sup>  
<sup>**7.** Dobin, A., et al., STAR: ultrafast universal RNA-seq aligner. Bioinformatics, 2013. 29(1): p. 15-21.</sup>  
<sup>**8.** Bushnell, B., Rood, J., & Singer, E. (2017). BBMerge - Accurate paired shotgun read merging via overlap. PloS one, 12(10), e0185056.</sup>  
<sup>**9.** Okonechnikov, K., et al. (2015). "Qualimap 2: advanced multi-sample quality control for high-throughput sequencing data." Bioinformatics 32(2): 292-294.</sup>  
<sup>**10.** The Picard toolkit. https://broadinstitute.github.io/picard/.</sup>  
<sup>**11.** Daley, T. and A.D. Smith, Predicting the molecular complexity of sequencing libraries. Nat Methods, 2013. 10(4): p. 325-7.</sup>  
<sup>**12.** Li, H., et al. (2009). "The Sequence Alignment/Map format and SAMtools." Bioinformatics 25(16): 2078-2079.</sup>  
<sup>**13.** Wang, L., et al. (2012). "RSeQC: quality control of RNA-seq experiments." Bioinformatics 28(16): 2184-2185.</sup>  
<sup>**14.** Li, B. and C.N. Dewey, RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome. BMC Bioinformatics, 2011. 12: p. 323.</sup>  
<sup>**15.** Uhrig, S., et al. (2021). "Accurate and efficient detection of gene fusions from RNA sequencing data". Genome Res. 31(3): 448-460.</sup>  
<sup>**16.** Ewels, P., et al. (2016). "MultiQC: summarize analysis results for multiple tools and samples in a single report." Bioinformatics 32(19): 3047-3048.</sup>

<!---
## Future Inclusions
<sup>**NA.**	Law, C.W., et al., voom: Precision weights unlock linear model analysis tools for RNA-seq read counts. Genome Biol, 2014. 15(2): p. R29.</sup>
<sup>**NA.**	Smyth, G.K., Linear models and empirical bayes methods for assessing differential expression in microarray experiments. Stat Appl Genet Mol Biol, 2004. 3: p. Article3.</sup>
<sup>**NA.**	Fabregat, A., et al., The Reactome Pathway Knowledgebase. Nucleic Acids Res, 2018. 46(D1): p. D649-D655.</sup>
<sup>**NA.**	Liberzon, A., et al., Molecular signatures database (MSigDB) 3.0. Bioinformatics, 2011. 27(12): p. 1739-40.</sup>
<sup>**NA.**    Love, M. I., et al. (2014). "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2." Genome Biol 15(12): 550.</sup>
<sup>**NA.**    R Core Team (2018). R: A Language and Environment for Statistical Computing. Vienna, Austria, R Foundation for Statistical Computing.</sup>
<sup>**NA.**    Leng, N., et al. (2013). "EBSeq: an empirical Bayes hierarchical model for inference in RNA-seq experiments." Bioinformatics 29(8): 1035-1043.</sup>
<sup>**NA.**    Robinson, M. D., et al. (2009). "edgeR: a Bioconductor package for differential expression analysis of digital gene expression data." Bioinformatics 26(1): 139-140.</sup>
--->
