from __init__ import *
import data.webscraping as scrape
import visualization.visualize as vi

print(datapath)
print(srcpath)
print(modelspath)

if False:
    blob = scrape.scraping()
    tit, data = scrape.decode(blob)
    df = scrape.data2df(tit, data)
if False:
    df = scrape.webscrape()
if True:
    df = scrape.webscrape()
    vi.Descrstats().plot_distribution(df, "smoking", 5)
    vi.Descrstats().plot_distribution(df, "length", 10)
    vi.Descrstats().plot_distribution(df, "mass", 10)
    vi.Descrstats().plot_distribution(df, "sugar", 4)
    vi.Descrstats().plot_distribution(df, "lifespan", 10)
    # vi.Descrstats().plot_xygraph(df, "length", "mass")
    # vi.Descrstats().plot_xygraph(df, "genetic", "exercise")
    # vi.Descrstats().plot_xygraph(df, "genetic", "smoking")
    # vi.Descrstats().plot_xygraph(df, "exercise", "alcohol")
    # vi.Descrstats().plot_xygraph(df, "smoking", "alcohol")

print(df)
