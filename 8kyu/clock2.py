def past(h, m, s):
  hour = h * 3600
  minute = m * 60
  second = s * 1

  time = (hour + minute + second) * 1000
  return time