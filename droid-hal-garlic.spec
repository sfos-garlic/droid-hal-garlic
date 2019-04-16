# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device garlic
%define vendor yu

%define vendor_pretty Yu
%define device_pretty Yureka Black

%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/bugreports\
/d\
/file_contexts.bin\
/init.qcom.sh\
/init.qcom.usb.sh\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

%define android_config \
#define QCOM_BSP 1\
#define QTI_BSP 1\
%{nil}
#Black gallery pictures and no browser content/browser crash

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

