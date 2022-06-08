class Solution:

    def roman_to_int(self, s: str) -> int:
        """
        :param s:
        :return:
        """
        symbole = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        nbr = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                c = symbole[s[i]]
                n = symbole[s[i + 1]]
                if c > n:
                    nbr += c
                    i += 1
                elif c == n:
                    nbr += c + n
                    i += 2
                else:
                    nbr += n - c
                    i += 2
            else:
                nbr += symbole[s[i]]
                i += 1
        return nbr
