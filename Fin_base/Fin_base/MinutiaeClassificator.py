import MinutiaeClassificator
#import ClassifyNetPathMissingException

minutiaeClassificator = MinutiaeClassificator
minutiaeClassificator.get_classify_net_path('"C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/f2.bmp')

#try:
minutiaeClassificator.load_classification_module()
#except ClassifyNetPathMissingException:
print('rttt')