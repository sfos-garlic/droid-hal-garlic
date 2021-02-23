# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device garlic
%define vendor yu

%define vendor_pretty Yu
%define device_pretty Yureka Black

%define installable_zip 1
%define rpm_device vince
%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define straggler_files \
    /acct \
    /charger \
    /bugreports \
    /d \
    /cache \
    /sdcard \
    /dsp \
    /firmware \
    /persist \
    /product \
    /odm \
    /system \
    /vendor \
    /oem \
    /vendor_file_contexts \
    /vendor_hwservice_contexts \
    /vendor_property_contexts \
    /vendor_seapp_contexts \
    /vendor_service_contexts \
    /vndservice_contexts \
    /plat_file_contexts \
    /plat_hwservice_contexts \
    /plat_property_contexts \
    /plat_seapp_contexts \
    /plat_service_contexts \
%{nil}

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

