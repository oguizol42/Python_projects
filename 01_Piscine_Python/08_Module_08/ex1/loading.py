import sys

try:
    print(f"Python executable: {sys.executable}")
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    import pandas

    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    import numpy

    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    import requests

    print(f"[OK] requests ({requests.__version__}) - Network access ready")
    import matplotlib
    import matplotlib.pyplot

    print(
        f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready\n"
    )

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = numpy.random.normal(0, 1, 1000)
    print("Generating visualization...")
    df = pandas.DataFrame(data, columns=["matrix_signal"])
    print(df.describe())
    print("\nAnalysis complete!")
    matplotlib.pyplot.hist(df["matrix_signal"], bins=50)
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")
except ImportError as e:
    print(e)
    print("\nTo install with pip, run:")
    print("pip install -r requirements.txt")
    print("python3 loading.py")
    print("\nTo install with Poetry, run:")
    print("poetry install")
    print("poetry run python loading.py")
