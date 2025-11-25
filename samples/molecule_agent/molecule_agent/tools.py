

def get_similar_molecules() -> str:
    molecules = """[
  {
    "Names": "zalcitabine; Dideoxycytidine; 7481-89-2; 2',3'-DIDEOXYCYTIDINE; HIVID",
    "CompoundCID": "24066",
    "MolecularFormula": "C9H13N3O3",
    "MolecularWeight": "211.22g/mol",
    "IUPACName": "4-amino-1-[(2R,5S)-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1C[C@@H](O[C@@H]1CO)N2C=CC(=NC2=O)N",
    "InChIKey": "WREGKURFCTUGRC-POYBYMJQSA-N",
    "InChI": "InChI=1S/C9H13N3O3/c10-7-3-4-12(9(14)11-7)8-2-1-6(5-13)15-8/h3-4,6,8,13H,1-2,5H2,(H2,10,11,14)/t6-,8+/m0/s1",
    "CreateDate": "2005-06-24"
  },
  {
    "Names": "gemcitabine; 95058-81-4; 2'-Deoxy-2',2'-difluorocytidine; 2',2'-Difluorodeoxycytidine; Gemcitabina",
    "CompoundCID": "60750",
    "MolecularFormula": "C9H11F2N3O4",
    "MolecularWeight": "263.2g/mol",
    "IUPACName": "4-amino-1-[(2R,4R,5R)-3,3-difluoro-4-hydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)[C@H]2C([C@@H]([C@H](O2)CO)O)(F)F",
    "InChIKey": "SDUQYLNIPVEERB-QPPQHZFASA-N",
    "InChI": "InChI=1S/C9H11F2N3O4/c10-9(11)6(16)4(3-15)18-7(9)14-2-1-5(12)13-8(14)17/h1-2,4,6-7,15-16H,3H2,(H2,12,13,17)/t4-,6-,7-/m1/s1",
    "CreateDate": "2005-06-24"
  },
  {
    "Names": "cytarabine; 147-94-4; Ara-C; Cytosine arabinoside; Aracytidine",
    "CompoundCID": "6253",
    "MolecularFormula": "C9H13N3O5",
    "MolecularWeight": "243.22g/mol",
    "IUPACName": "4-amino-1-[(2R,3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)[C@H]2[C@H]([C@@H]([C@H](O2)CO)O)O",
    "InChIKey": "UHDGCWIWMRVCDJ-CCXZUQQUSA-N",
    "InChI": "InChI=1S/C9H13N3O5/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16)/t4-,6-,7+,8-/m1/s1",
    "CreateDate": "2005-06-24"
  },
  {
    "Names": "cytidine; 65-46-3; Cytosine riboside; 1-beta-D-Ribofuranosylcytosine; 4-Amino-1-beta-D-ribofuranosyl-2(1H)-pyrimidinone",
    "CompoundCID": "6175",
    "MolecularFormula": "C9H13N3O5",
    "MolecularWeight": "243.22g/mol",
    "IUPACName": "4-amino-1-[(2R,3R,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)[C@H]2[C@@H]([C@@H]([C@H](O2)CO)O)O",
    "InChIKey": "UHDGCWIWMRVCDJ-XVFCMESISA-N",
    "InChI": "InChI=1S/C9H13N3O5/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16)/t4-,6-,7-,8-/m1/s1",
    "CreateDate": "2004-09-16"
  },
  {
    "Names": "2'-deoxycytidine; deoxycytidine; 951-77-9; CYTIDINE, 2'-DEOXY-; Deoxyribose cytidine",
    "CompoundCID": "13711",
    "MolecularFormula": "C9H13N3O4",
    "MolecularWeight": "227.22g/mol",
    "IUPACName": "4-amino-1-[(2R,4S,5R)-4-hydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1[C@@H]([C@H](O[C@H]1N2C=CC(=NC2=O)N)CO)O",
    "InChIKey": "CKTSBUTUHBMZGZ-SHYZEUOFSA-N",
    "InChI": "InChI=1S/C9H13N3O4/c10-7-1-2-12(9(15)11-7)8-3-5(14)6(4-13)16-8/h1-2,5-6,8,13-14H,3-4H2,(H2,10,11,15)/t5-,6+,8+/m0/s1",
    "CreateDate": "2005-06-01"
  },
  {
    "Names": "Cytosar; 478511-21-6; [5',5''-2H2]cytidine; 4-amino-1-pentofuranosylpyrimidin-2(1H)-one; .beta.-Arabinosylcytosine",
    "CompoundCID": "596",
    "MolecularFormula": "C9H13N3O5",
    "MolecularWeight": "243.22g/mol",
    "IUPACName": "4-amino-1-[3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)C2C(C(C(O2)CO)O)O",
    "InChIKey": "UHDGCWIWMRVCDJ-UHFFFAOYSA-N",
    "InChI": "InChI=1S/C9H13N3O5/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16)",
    "CreateDate": "2005-03-25"
  },
  {
    "Names": "CYTARABINE HYDROCHLORIDE; Cytosine arabinoside hydrochloride; 69-74-9; Cytarabine HCl; Ara-C hydrochloride",
    "CompoundCID": "6252",
    "MolecularFormula": "C9H14ClN3O5",
    "MolecularWeight": "279.68g/mol",
    "IUPACName": "4-amino-1-[(2R,3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one;hydrochloride",
    "SMILES": "C1=CN(C(=O)N=C1N)[C@H]2[C@H]([C@@H]([C@H](O2)CO)O)O.Cl",
    "InChIKey": "KCURWTAZOZXKSJ-JBMRGDGGSA-N",
    "InChI": "InChI=1S/C9H13N3O5.ClH/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8;/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16);1H/t4-,6-,7+,8-;/m1./s1",
    "CreateDate": "2005-07-19"
  },
  {
    "Names": "GEMCITABINE HYDROCHLORIDE; 122111-03-9; Gemcitabine HCl; Gemzar; LY188011 hydrochloride",
    "CompoundCID": "60749",
    "MolecularFormula": "C9H12ClF2N3O4",
    "MolecularWeight": "299.66g/mol",
    "IUPACName": "4-amino-1-[(2R,4R,5R)-3,3-difluoro-4-hydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one;hydrochloride",
    "SMILES": "C1=CN(C(=O)N=C1N)[C@H]2C([C@@H]([C@H](O2)CO)O)(F)F.Cl",
    "InChIKey": "OKKDEIYWILRZIA-OSZBKLCCSA-N",
    "InChI": "InChI=1S/C9H11F2N3O4.ClH/c10-9(11)6(16)4(3-15)18-7(9)14-2-1-5(12)13-8(14)17;/h1-2,4,6-7,15-16H,3H2,(H2,12,13,17);1H/t4-,6-,7-;/m1./s1",
    "CreateDate": "2005-06-24"
  },
  {
    "Names": "Arabinofuranosylcytosine; 3083-52-1; 4-amino-1-[(3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one; Arabinosylcytosine; Citozar",
    "CompoundCID": "114682",
    "MolecularFormula": "C9H13N3O5",
    "MolecularWeight": "243.22g/mol",
    "IUPACName": "4-amino-1-[(3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)C2[C@H]([C@@H]([C@H](O2)CO)O)O",
    "InChIKey": "UHDGCWIWMRVCDJ-STUHELBRSA-N",
    "InChI": "InChI=1S/C9H13N3O5/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16)/t4-,6-,7+,8?/m1/s1",
    "CreateDate": "2005-06-01"
  },
  {
    "Names": "Endalin; 2',3'-Dideoxy-5-fluorocytidine; MLS003389356; SMR002049011; Endoxin",
    "CompoundCID": "355450",
    "MolecularFormula": "C9H12FN3O3",
    "MolecularWeight": "229.21g/mol",
    "IUPACName": "4-amino-5-fluoro-1-[5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1CC(OC1CO)N2C=C(C(=NC2=O)N)F",
    "InChIKey": "QBEIABZPRBJOFU-UHFFFAOYSA-N",
    "InChI": "InChI=1S/C9H12FN3O3/c10-6-3-13(9(15)12-8(6)11)7-2-1-5(4-14)16-7/h3,5,7,14H,1-2,4H2,(H2,11,12,15)",
    "CreateDate": "2005-03-26"
  },
  {
    "Names": "Arabinofuranosylcytosine; 3083-52-1; 4-amino-1-[(3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one; Arabinosylcytosine; Citozar",
    "CompoundCID": "114682",
    "MolecularFormula": "C9H13N3O5",
    "MolecularWeight": "243.22g/mol",
    "IUPACName": "4-amino-1-[(3S,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one",
    "SMILES": "C1=CN(C(=O)N=C1N)C2[C@H]([C@@H]([C@H](O2)CO)O)O",
    "InChIKey": "UHDGCWIWMRVCDJ-STUHELBRSA-N",
    "InChI": "InChI=1S/C9H13N3O5/c10-5-1-2-12(9(16)11-5)8-7(15)6(14)4(3-13)17-8/h1-2,4,6-8,13-15H,3H2,(H2,10,11,16)/t4-,6-,7+,8?/m1/s1",
    "CreateDate": "2005-06-01"
  }
]"""
    return molecules


