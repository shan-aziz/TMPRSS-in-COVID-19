# Structural and Functional Features of the Transmembrane Serine Proteases – Implications in Viral Pathogenesis

### Author: Shan Aziz  
**Institution:** Department of Natural Sciences and Mathematics, The University of Texas at Dallas  
**Instructor:** Dr. Mehmet Candas

---

## 📄 Abstract

This project presents homology modeling and docking analyses of the transmembrane serine protease (TMPRSS) family, with a focus on TMPRSS2 due to its key role in facilitating viral entry, including SARS-CoV-2. The study identifies potential drug binding pockets and highlights amino acid differences that could enable selective drug targeting. These insights are vital for therapeutic development against viral diseases and related cancers.

---

## 🧬 Introduction

Transmembrane serine proteases (TMPRSS) are a family of enzymes critical for physiological processes like coagulation, digestion, and viral entry. Several TMPRSS members, particularly TMPRSS2 and TMPRSS4, are involved in activating viral proteins such as the SARS-CoV-2 spike protein. Due to the lack of experimentally derived crystal structures, this study builds structural models using homology modeling and performs molecular docking to identify druggable sites.

---

## 🧪 Methods

### 🔗 Sequence and Structure Modeling
- Amino acid sequences for 14 TMPRSS proteins were retrieved from UniProt.
- Templates identified via BLASTp and PDB.
- Homology models constructed using Modeller.
- Structural evaluation via SAVES v6.0.

### 🧬 Molecular Docking
- Docking performed with CB-Dock2.
- Ligands (e.g., Camostat) sourced from PubChem.
- Binding pockets (C1–C5) characterized based on docking scores and contact residues.
- Structural alignment performed to compare conserved catalytic triads.

---

## 📊 Results

### ✅ Homology Models
- Successfully built homology models for 14 TMPRSS family members.
- Trypsin-like serine protease domains conserved with high identity (>40%).

### 🔍 Pocket Identification
- 5 major binding pockets (C1–C5) identified in TMPRSS2.
- Pocket C4’s Lysine-87 found critical for Camostat metabolite (GBPA) binding.
- Residue variation across TMPRSS proteins may allow for selective inhibitor design.

### 🧪 Docking Highlights
| Pocket | Vina Score | Contact Residues Highlight |
|--------|------------|-----------------------------|
| C1     | -6.8       | HIS41, LYS85, LYS87, SER181 |
| C2     | -6.7       | HIS19, VAL25, GLN62         |
| C3     | -6.5       | PRO9, PHE64, TYR71          |
| C4     | -6.3       | LYS87 (key for GBPA)        |
| C5     | -6.1       | TRP14, TRP125, ALA144       |

---

## 🧠 Discussion

- **Selectivity Opportunity:** Only TMPRSS2 and TMPRSS4 conserve Lys87 in Pocket C4, a key GBPA binding site.
- **Drug Development:** Understanding these structural differences can help design selective inhibitors that minimize off-target effects.
- **Viral Entry Inhibition:** Structural targeting of TMPRSS2 can block SARS-CoV-2 entry and potentially reduce COVID-19 virulence.

---

## ✅ Conclusion

This project reveals structural insights into TMPRSS proteases and their roles in viral infection. It highlights unique residues critical for drug binding and identifies TMPRSS2/4 as key targets for selective inhibition. These findings could aid in the development of antiviral therapeutics and cancer treatments by exploiting conserved structural motifs and binding pockets.

---

## 🔗 Resources

- **CB-Dock2**: [https://cadd.labshare.cn/cb-dock2/php/manual.php](https://cadd.labshare.cn/cb-dock2/php/manual.php)  
- **PubChem**: [https://pubchem.ncbi.nlm.nih.gov/](https://pubchem.ncbi.nlm.nih.gov/)

---

## 📚 References

A comprehensive list of references is provided in the [References](#) section of the original document, covering foundational studies on TMPRSS structure, viral pathogenesis, and drug binding interactions.

---

## 📁 Supplementary Information

- Full list of PDB templates used  
- Sequence alignments (Jalview screenshots)  
- Structural visualizations (Figs 1–6)  
- Table A (TMPRSS functions)  
- Table B (Docking scores & residues)  
- Homology models (hmTMPRSSx)

---

## 🧑‍💻 Future Work

- Incorporate AI-based structural refinement (e.g., AlphaFold2)
- Validate docking with experimental binding assays
- Expand analysis to other viral pathogens using TMPRSS family for entry

---

## 💬 Feedback & Collaboration

Feel free to open issues or contact me for collaboration ideas or suggestions!

---
