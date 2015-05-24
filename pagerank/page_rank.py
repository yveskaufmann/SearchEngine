from model.page import Pages

__author__ = 'hannah'


class Page_Rank(object):

    matrix = []
    page_rank = []
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
        #for row in self.matrix:
        #    print(row)
    #
    # def count_true(self, row):
    #     count_true = 0
    #     for col in self.matrix[row]:
    #         if col is True:
    #             count_true += 1
    #     return count_true

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
        for row in self.matrix:
            print(row)

    def calculate_page_rank(self, convergence):
        tmp_pr = [i for i in range(len(self.pages.data))]
        step0 = 1/len(self.matrix)
        for i in self.pages.data:
            i.page_rank = step0
        diff = 1.0
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
            count = 0
            for i in tmp_pr:
                self.pages.data[count].page_rank = i
                count += 1
            count = 0
            diff = 0
            for i in self.pages.data:
                diff += abs(tmp_pr[count] - i.page_rank)
                count += 1





        # step = 0
        # count_row = 0
        # for row in range(len(self.matrix)):
        #     step0 = 1/len(self.matrix)
        #     self.page_rank.append(step0)
        #     count_row += 1
        # print("Step : ", step, self.page_rank)
        # step = 1
        # diff = 1.0
        # while diff > convergence:
        #     pr_col = []
        #     for step in range(1, len(self.page_rank)):
        #         pr_col.append(step)
        #         for col in pr_col:
        #             #self.page_rank[step].append(pr_col)
        #             print(col)
        #             col += 1
        #             for row in range(len(self.page_rank)):
        #                 #val = step0 * (self.matrix[row][col])
        #                 row += 1
        #                 # self.page_rank[step][col] = val
        #             #self.page_rank[step].append(val)
        #     step += 1
        #     diff -= 0.1
        # print("Step : ", step, self.page_rank)
        # # for i in self.page_rank:
        # #     print(i)

    def set_page_rank(self):
        pass
# print(self.page_rank[self.page_rank.index(count_col)])
#                     pr = count_col * self.matrix[0][0] + self.page_rank[count_col+1] * self.matrix[1][0] #+ self.page_rank[col+2] * self.matrix[2][0]
#                     self.page_rank.append(pr)#[count_row][count_col] = pr
#crawler = Crawler()
#bla = Page_Rank()
#print(bla.fill_matrix(crawler))
#print(bla.calculate_probabilities(0.05, 0.95))


        #diff = 1
        #count_row = 0
        # for row in self.matrix:
        #     count_col = 0
        #     for col in row:
        #         val = 1/len(self.matrix)
        #         count_col += 1
        #     count_row += 1
        #     self.page_rank[count_row].append(val)
        # for step in self.page_rank:
        #     print(step)


        # def print_matrix(crawler_result):
        #    matrix = []
        #    for x in range(crawler_result.pages.count()):  #
        #        matrix.append(crawler_result.pages.data[x].out_links) #crawler_result.pages.count()
        #    for row in matrix:
        #        print(row)
        # print(crawler_result.pages.data[0].out_links)
        #    print(crawler_result.pages.count())
        #    print(matrix)

        # def fill_matrix(crawler_result):
        #    matrix = []
        #    for x in range(crawler_result.pages.count()):
        #        if x is not crawler_result.pages.data[x].out_links:
        #            matrix.append(0)
        #        else:
        #            matrix.append(crawler_result.pages.data[x].out_links)

        # for row in matrix:#
        #        print(" ".join(matrix[row]))

        # def test_bla(crawler_result):
        #    for x in range(crawler_result.pages.count()):
        #        matrix = []
        #        matrix.append(crawler_result.pages.get_page_by_url(crawler_result.pages.data[x]))
        #    for row in matrix:
        #        print(" ".join(matrix[row]))


        # crawler_result.page.out_pages.has_page_with_title


        # outpage.title == 'd0' + col



        #    if i in crawler_result.pages.data[i].out_links
        #   row = crawler_result.pages.data[i].out_links
        #  col = crawler_result.pages.data[i].out.links[j]

        # matrix = [[i for i in crawler_result.pages.data[i].out_links] for j in crawler_result.pages.data[i].out_links[j]]
        # for i in range(8):
        #     for j in range(8):
        #         # to-do if-abfrage, ob da outlinks drin sind
        #         matrix[i][j] = crawler.pages.data[i].out_links[j]
        # return matrix

        # if i in matrix is 0
        # count = 0.0
        # count = count+1 in matrix[0]
        # if matrix[0][0] == 1:
        #    matrix[0][0] = d/count + (t/n)#

        # if matrix[0][0] == 0:
        #   matrix[0][0] = t/n

        # for i,j in

        # matrix = [[0 for i in range(8)],[0 for j in range(8)]]

        # print(fill_matrix(crawler))
