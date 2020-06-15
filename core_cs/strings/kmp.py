# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    pattern_length = len(pat)
    text_length = len(txt)
    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * pattern_length
    pattern_index = 0  # index for pat[]
    text_index = 0  # index for txt[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, pattern_length, lps)

    while text_index < text_length:
        if pat[pattern_index] == txt[text_index]:
            text_index += 1
            pattern_index += 1

        if pattern_index == pattern_length:
            print("Found pattern at index " + str(text_index - pattern_index))
            pattern_index = lps[pattern_index - 1]
        # mismatch after j matches
        elif text_index < text_length and pat[pattern_index] != txt[text_index]:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1


def computeLPSArray(pat, pattern_length, lps):
    lps_length = 0  # length of the previous longest prefix suffix
    pattern_index = 1

    while pattern_index < pattern_length:
        # We are either setting the lps to lps_length or to 0
        # If it matches
        if pat[pattern_index] == pat[lps_length]:
            lps_length += 1
            lps[pattern_index] = lps_length
            pattern_index += 1
        else:
            # If it doesnt
            # case 1: if lps_length is not zero
            if lps_length != 0:
                lps_length = lps[lps_length - 1]
            # case 2: if lps_length is zero
            else:
                lps[pattern_index] = 0
                pattern_index += 1


if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABAB"
    KMPSearch(pat, txt)





