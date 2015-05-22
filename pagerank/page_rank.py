from crawler.Crawler import Crawler
#from model.page import Page

__author__ = 'hannah'

# crawler.pages.data[0].out_links   -> array mit allen outlinks der 1. seite

# crawler.pages.data[3].out_links[0] -> der 1. out_link der 4. seite



class Page_Rank(object):

    matrix = []

    def fill_matrix(self, crawler_data):
        row = 0
        for page in crawler_data.pages:
            outlinks = []
            for c in range(1, crawler_data.pages.count() + 1):
                title = "d0" + str(c)
                outlinks.append(page.out_pages.has_page_with_title(title))
            self.matrix.append(outlinks)
            row += 1
        for row in self.matrix:
            print(row)

    def count_true(self, row):
        count_true = 0
        for col in self.matrix[row]:
            if col is True:
                count_true += 1
        return count_true

    def calculate_probabilities(self, teleportation, damping):
        count_row = 0
        for row in self.matrix:
            count_col = 0
            for col in row:
                if col is False:
                    self.matrix[count_row][count_col] = (teleportation/len(row))
                else:
                    if col is True:
                        damp = (damping/self.count_true(count_row))
                        self.matrix[count_row][count_col] = damp + (teleportation/len(row))
                count_col += 1
            count_row += 1
        for row in self.matrix:
            print(row)

    def calculate_page_rank(self, outlinks, teleportation, damping, convergence):
        pass

crawler = Crawler()
bla = Page_Rank()
print(bla.fill_matrix(crawler))
print(bla.calculate_probabilities(0.05, 0.95))





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
