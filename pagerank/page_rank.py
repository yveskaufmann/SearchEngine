from model.page import Pages

__author__ = 'hannah'

class Page_Rank(object):

    matrix = []
    pages = Pages()

    def fill_matrix(self, crawler_data):
        self.pages = crawler_data.pages
        row = 0
        for page in crawler_data.pages:
            outlinks = []
            for c in range(1, crawler_data.pages.count() + 1):
                title = "d0" + str(c)
                outlinks.append(page.out_pages.has_page_with_title(title))
            self.matrix.append(outlinks)
            row += 1

    def calculate_probabilities(self, teleportation, damping):
        count_row = 0
        for row in self.matrix:
            count_col = 0
            if len(self.pages.data[count_row].out_links) != 0:
                for col in row:
                    if col is False:
                        self.matrix[count_row][count_col] = (teleportation/len(row))
                    else:
                        if col is True:
                            count_outlinks = len(self.pages.data[count_row].out_links)
                            damp = ((1.0/count_outlinks) * damping)
                            self.matrix[count_row][count_col] = damp + (teleportation/len(row))
                    count_col += 1
                count_row += 1
            else:
                for col in row:
                    self.matrix[count_row][count_col] = 1.0/len(row)
                    count_col += 1

    def calculate_page_rank(self, convergence):
        print("Page Rank \n¯¯¯¯¯¯¯¯¯")
        print("            d01     d02     d03     d04     d05     d06     d07     d08     diff")
        tmp_pr = [i for i in range(len(self.pages.data))]
        out_put = []
        step0 = 1/len(self.matrix)
        for i in self.pages.data:
            i.page_rank = step0
            out_put.append(i.page_rank)
        print("step :  0", out_put)
        # for each in self.pages.data:
        #     print(round(each.page_rank, 4))
        diff = 1.0
        count_step = 1
        while diff > convergence:
            col = 0
            for lila in self.pages.data:
                tmp = 0
                row = 0
                for gelb in self.pages.data:
                    bla = self.matrix[row][col]
                    tmp += gelb.page_rank * self.matrix[row][col]
                    row += 1
                tmp_pr[col] = tmp
                col += 1
            diff = 0
            count = 0
            for i in self.pages.data:
                diff += abs(tmp_pr[count] - i.page_rank)
                count += 1
            count = 0
            out_put = []
            for i in tmp_pr:
                self.pages.data[count].page_rank = i
                count += 1
                out_put.append(round(i, 4))
            print("step : ", count_step, out_put, round(diff, 4))
            count_step += 1