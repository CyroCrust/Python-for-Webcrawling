text = "X-DSPAM-Confidence:    0.8475";
fcol = text.find('0')
fspace = text.find('5')
final = text[fcol:fspace+1]
print(float(final))
