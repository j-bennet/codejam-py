def subsetsum(nums, tgt):
  sums = {}
  for n in nums[::2]:
      for k,v in sums.items() + [(0,[])]:
          newsum = k + n
          if newsum not in sums:
              sums[newsum] = v + [n]
              if newsum == tgt:
                  return sums[tgt]

  difs = {tgt:[]}
  for n in nums[1::2]:
      for k,v in difs.items():
          newdif = k - n
          if newdif not in difs:
              difs[newdif] = v + [n]
              if newdif in sums:
                  return sums[newdif] + difs[newdif]

    return []
