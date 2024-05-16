def samitleri_al(yoxlanacaq_soz):
  samitler = set()
  for harf in yoxlanacaq_soz:
    if harf.lower() not in 'aeiou' and harf.isalpha():
       samitler.add(harf.lower())
  return samitler


