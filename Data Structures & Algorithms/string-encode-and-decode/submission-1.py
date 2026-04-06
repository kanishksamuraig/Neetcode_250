class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr=""
        for i in strs:
            encodedstr+=str(len(i))+"#"+i
        return encodedstr
    def decode(self, s: str) -> List[str]:
        print(s)
        decodedlst=[]
        flag=False
        i=0
        while(i<len(s)):
            num=""
            j=i
            while(s[j]!="#"):
                num+=s[j]
                j+=1
            print(num)
            if num=="0":
                decodedlst.append("")
                i+=2
                continue
            word=""
            for k in range(j+1,j+int(num)+1):
                word+=s[k]
            decodedlst.append(word)
            i=k+1
        return decodedlst

            