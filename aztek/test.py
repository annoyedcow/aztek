class Test:
    def output(self, df):        
        def highlight(row):
            def colored(color):
                cols = []
                for r in range(row.size):
                    cols.append(color)
                return cols

            red = "background-color: indianred;"
            return colored(red)   
        df = df.style.apply(highlight, axis=1)
        display(df)

def printdf():
    import pandas as pd
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    
    t = Test()
    t.output(df)


class Test2:
    def highlight(self, row):
        def colored(color):
            cols = []
            for r in range(row.size):
                cols.append(color)
            return cols

        red = "background-color: indianred;"
        return colored(red)   
    
def printdf2():
    import pandas as pd
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    
    t = Test2()
    sty = df.style.apply(t.highlight, axis=1)
    display(sty)
    

