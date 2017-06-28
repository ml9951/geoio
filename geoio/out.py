--- dg.py	(original)
+++ dg.py	(refactored)
@@ -21,7 +21,7 @@
 
 import tinytools as tt
 from .base import GeoImage
-import constants as const
+from . import constants as const
 
 # Module setup
 logger = logging.getLogger(__name__)
@@ -151,7 +151,7 @@
         self.meta_dg = tt.bunch.ordered_bunchify(tmp_dict['ISD'])
 
     def _update_dict_differences(self,d,input=None,output=None):
-        for x in d.keys():
+        for x in list(d.keys()):
             if x == input:
                 d[output.upper()] = d.pop(x)
                 x = output.upper()
@@ -438,7 +438,7 @@
         and effective bandwidths are pull from the IMD files for each image."""
 
         if not band_nums:
-            band_nums = range(data.shape[0])
+            band_nums = list(range(data.shape[0]))
         else:
             band_nums = [x-1 for x in band_nums]
             if len(band_nums) != data.shape[0]:
@@ -492,7 +492,7 @@
         """
 
         if not band_nums:
-            band_nums = range(data.shape[0])
+            band_nums = list(range(data.shape[0]))
         else:
             band_nums = [x-1 for x in band_nums]
             if len(band_nums) != data.shape[0]:
@@ -632,7 +632,7 @@
                 for i in flist_for_vrt: cmd.append(i)
                 tt.cmd_line.exec_cmd(cmd)
                 if not os.path.isfile(vrt_name):
-                   raise StandardError("Creation of file "+vrt_name+" "
+                   raise Exception("Creation of file "+vrt_name+" "
                                        "failed. This could possibly be a "
                                        "write access problem?")
 
@@ -687,7 +687,7 @@
                 for i in flist_for_vrt: cmd.append(i)
                 tt.cmd_line.exec_cmd(cmd)
                 if not os.path.isfile(vrt_name):
-                   raise StandardError("Creation of file "+vrt_name+" "
+                   raise Exception("Creation of file "+vrt_name+" "
                                        "failed. This could possibly be a "
                                        "write access problem?")
 
