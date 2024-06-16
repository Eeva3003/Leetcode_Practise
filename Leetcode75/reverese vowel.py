class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = "aeiouAEIOU"  # Set of vowels for easier checking instead of using or statemnt in if statement 
    l = 0
    r = len(s) - 1
    s = list(s)  # Convert string to list for modification

    while r >= l:
      # Check if characters are vowels
      if s[l] in vowels and s[r] in vowels:
        s[l], s[r] = s[r], s[l]  # Swap vowels
        l += 1
        r -= 1
      else:
        # Move pointers if not vowels
        if s[l] not in vowels:
          l += 1
        if s[r] not in vowels:
          r -= 1

    return ''.join(s)  # Join list back to string
#joining instead of converting back with str function
