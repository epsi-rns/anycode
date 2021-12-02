# additional function

def wedge_text(percent, total):
    absolute = int(round(total*percent/100))
    if percent > 10:
      return "{:.1f}%\n({:d})".format(percent, absolute)
    else:
      return ""
