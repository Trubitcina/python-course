from itertools import islice
import re


def ListsToDict(list1, list2):
    d = dict(zip(list1, map(float, list2)))
    return(d)


def OpenScores(path):
    with open(path, 'r') as f:
        header = f.readline().strip()
        header = header.split('\t')[1:]
        output = {}
        for line in islice(f, 0, len(header)):
            line = line.strip()
            line = line.split('\t')
            output.update({line[0]: ListsToDict(header, line[1:])})
        return(output)


def NCstrand(ArchSequence, ArchType):  # make list(Nstrand, Cstrand)
    if re.search("\d", ArchType) is None:
        n = int((len(ArchSequence) - len(ArchType)) / 2)
    else:
        re.findall("\d", ArchType)
        ArchType = int(list(ArchType)[0])
        n = int((len(ArchSequence) - ArchType)/2)
    NClist = []
    NClist.append(ArchSequence[:n])
    NClist.append(ArchSequence[-n:])
    return(NClist)


def GiveScores(strand1, strand2):
    inner = OpenScores("steny_in.txt")
    outer = OpenScores("steny_out.txt")
    Scores_in = []
    Scores_out = []

    for i in range(len(strand1)):
        if i % 2 == 0:
            Scores_in.append(inner[strand1[i]][strand2[i]])

        else:
            Scores_out.append(outer[strand1[i]][strand2[i]])

    Scores = [sum(Scores_in) / len(Scores_in), sum(Scores_out) / len(Scores_out)]
    return(Scores)


def MakeDict(path):  # import from ArchCandy file, make dict of type {ArchNumber: [ArchSequence, ArchType]}
    with open(path, "r") as f:
        find = re.findall("\d+\s+[A-Z]+\s+\d.\d+\s+\w*\s\w*\s\w*\s\w*", f.read())
    f.close()
    arches = dict()
    a = 1
    for i in find:
        i = re.sub("\s+", " ", i.strip())
        i = re.sub("\s\d.\d\d\d\s", "\t", i)
        find_number = re.findall('^\d+', i)
        find_seq = re.findall("[A-Z]+\s", i)
        for n in find_seq:
            n.strip()
        find_type = re.findall("\t\w+\s*\w*\s*\w*\s*\w*", i)
        for m in find_type:
            m.strip()

        for k in find_number:
            arches[a] = n.strip(), m.strip()
            a += 1
    return(arches)


def PlayWithScores(seq1, ArchType1, seq2, ArchType2):
    Sarch = OpenScores("svody.txt")[ArchType1][ArchType2]
    Nseq1 = NCstrand(seq1, ArchType1)[0]
    Cseq1 = NCstrand(seq1, ArchType1)[1]
    Nseq2 = NCstrand(seq2, ArchType2)[0]
    Cseq2 = NCstrand(seq2, ArchType2)[1]

    ListScoresIn = []
    ListScoresOut = []
    ListFinalScores = []

    for i in range(3, len(Cseq2) + 1, 2):
        tmp1 = GiveScores(Nseq1[:i], Nseq2[:i])
        tmp2 = GiveScores(Cseq1[:i], Cseq2[:i])
        ListScoresIn.append((tmp1[0] + tmp2[0]) / 2)
        ListScoresOut.append((tmp1[1] + tmp1[1]) / 2)

    for i in range(len(ListScoresIn)):
        ListFinalScores.append(ListScoresIn[i] * ListScoresOut[i] * Sarch)
    return(max(ListFinalScores))


def group(matrix, count):
    return zip(*[iter(matrix)] * count)


OutputFile = open("output.txt", "w")


def FinalMatrix(path1, path2):
    matrix = []
    list1 = MakeDict(path1).values()
    list2 = MakeDict(path2).values()
    for i in list1:
        for j in list2:
            matrix.append(PlayWithScores(i[0], i[1], j[0], j[1]))
    # print(matrix)
    for i in group(matrix, 61):  # input № of arch of one with whom to compare, get 59 lines in table (as in S.cer)
        OutputFile.write('\t'.join(map(str, i)) + "\n")
    OutputFile.close()


FinalMatrix("SUP35N_P50Y_Sbay.txt", "SUP35N_Scer.txt")  # S.cer = columns, S.compare - rows
