
'''
xml files from TAB annotations and their correspoing WSI from Camelyon16 abnormal class of training set are used to create binary masks of the annotated regions.
multiresolutionimageinterface needs to be installed to run the following code. 
This code is directly taken from Camelyon16 dataset website'''

import os
import multiresolutionimageinterface as mir

# Following paths are provided for ease of use. Please change the paths according to your location and directory sructure
wsi_path = "D:\\Camelyon16\\Abnormal\\tumor_034.tif"
xml_path = "D:\\Camelyon16\\Annotations\\Tissue\T_tumor_034.xml"
mask_dest_dir = "D:\\Camelyon16\\Masks\\Tissue"
wsi_name = "tumor_034"

reader = mir.MultiResolutionImageReader()
mr_image = reader.open(wsi_path)  #<Path to WSI file stored as .tif>
annotation_list = mir.AnnotationList()
xml_repository = mir.XmlRepository(annotation_list)
xml_repository.setSource(xml_path)  # <Path to .xml file>
xml_repository.load()

annotation_mask = mir.AnnotationToMask()
output_path = os.path.join(mask_dest_dir, wsi_name + "_mask.tif")

label_map = {"_0": 1, '_1': 1, '_2': 1}
conversion_order = ["_0", '_1', '_2']
annotation_mask.convert(
    annotation_list,
    output_path,             # in the form "*\tumor_034_mask.tif"
    mr_image.getDimensions(),
    mr_image.getSpacing(),
    label_map,
    conversion_order
)

print(f"Mask saved: {output_path}")



