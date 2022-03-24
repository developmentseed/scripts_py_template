from smart_open import open
import json
from geojson import FeatureCollection
from shapely.geometry import shape


def read_geojson(input_file):
    """Read a geojson file and return a list of features

    Args:
        input_file (str): Location on geojson file

    Returns:
        list: list fo features
    """
    fc = []
    with open(input_file, "r", encoding="utf8") as f:
        cf = json.load(f)["features"]
    return cf


def write_geojson(output_file, list_features):
    """Write geojson files

    Args:
        output_file (str): Location of ouput file
        list_features (list): List of features
    """
    with open(output_file, "w") as f:
        json.dump(FeatureCollection(list_features), f)


def check_geometry(feature):
    """Verify if geometry is valid

    Args:
        feat (obj): Feature

    Returns:
        Bool: Return false or true acoording to the geometry
    """
    try:
        geom_shape = shape(feature["geometry"])
        return geom_shape.is_valid
    except Exception:
        return False
