import glob
import shapefile

def test():
    files = glob.glob("*/*.shp")
    w = shapefile.Writer()

    for f in files:
        r = shapefile.Reader(f)
        w._shapes.extend(r.shapes())
        w.records.extend(r.records())
    w.fields = list(r.fields)
    w.save("merged")
