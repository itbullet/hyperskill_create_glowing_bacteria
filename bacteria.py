class Bacteria:
    def __init__(self):
        self.strand1 = None
        self.strand2 = None
        self.strand1_sliced = None
        self.strand2_sliced = None
        self.site_location = None
        self.counter_plasmids = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            ' ': ' '
        }

    def complementary_strand(self, seq):
        complementary_seq = [self.counter_plasmids[char] for char in seq]
        complementary_seq_str = ''.join(complementary_seq)
        return complementary_seq_str

    def find_restriction_site(self, strand, site, side='left'):
        if side == 'right':
            self.site_location = strand.rfind(site)
        else:
            self.site_location = strand.find(site)
        return self.site_location

    def main(self):
        with open(input(), 'r') as file:
            data = file.read().split('\n')
            self.strand1 = data[0]
            site1 = data[1]
            gfp_strand = data[2]
            gfp_site1, gfp_site2 = data[3].split()
        cut_index1 = self.find_restriction_site(self.strand1, site1) + 1
        gfp_cut_index1 = self.find_restriction_site(gfp_strand, gfp_site1) + 1
        gfp_cut_index2 = self.find_restriction_site(gfp_strand, gfp_site2, 'right') + 1
        strand1_str = self.strand1[:cut_index1] + gfp_strand[gfp_cut_index1:gfp_cut_index2] + self.strand1[cut_index1:]
        print(strand1_str)

        print(self.complementary_strand(strand1_str))
        
        # self.strand2 = self.complementary_strand(self.strand1)
        # site1 = self.complementary_strand(site1)
        # gfp_strand = self.complementary_strand(gfp_strand)
        # gfp_site1 = self.complementary_strand(gfp_site1)
        # gfp_site2 = self.complementary_strand(gfp_site2)
        # cut_index1 = self.find_restriction_site(self.strand2, site1) + len(site1) - 1
        # gfp_cut_index1 = self.find_restriction_site(gfp_strand, gfp_site1) + len(gfp_site1) - 1
        # gfp_cut_index2 = self.find_restriction_site(gfp_strand, gfp_site2, 'right') + len(gfp_site2) - 1
        # print(f'{self.strand2[:cut_index1]}{gfp_strand[gfp_cut_index1:gfp_cut_index2]}{self.strand2[cut_index1:]}')


if __name__ == "__main__":
    Bacteria().main()



