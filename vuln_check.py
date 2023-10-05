import pkg_resources
from colorama import Fore, Style


packages = [
        "pywarder", "pyward", "syscolouringsaddv2", "syssqllibaryv1",
        "pipcryptographymodv1", "pythoncoloringpackage", "pythonfontingkitsv2",
        "pythonfontsliberyv1", "syscolouringexts", "pyfontstools",
        "pythonsqliteext", "syscolouringpkgv2", "syscryptographyadd",
        "syscryptographyv1", "pysqlilibery", "pythonsqlite3libaryv1",
        "pipcolourpkgs", "pipsqlitedbkit", "pipsqliteexts", "pythoncolourmodulev2",
        "pipcoloringsliberyv1", "pipcolouringext", "pycoloringextensionv1",
        "pycolorpkgsv2", "pycolouringskitv1", "pipcryptkits", "pipfontinglibv2",
        "pipsqladdv1", "pipsqlipackages", "pipsqlite3mod", "pipsqlitekitv2",
        "pycryptographypackagev1", "pysqlite3extensionv2", "pythoncolourextension",
        "pythoncolouringsliberyv1", "pythoncolouringtoolkitsv2", "pythonfontingadds",
        "pythonsqlitedbpackagesv2", "pythonsqlitetoolkitv1", "pythonsqltoolkitv1",
        "syssqllib", "pipcoloringstools", "pythoncryptextensions", "pitutil", "pitutils",
        "syscoloringsaddition", "syssqlitedbmodules", "sysfontstoolv1",
        "pycolouringsextv1", "pysqlite3extv2", "pipcoloringskitsv1", "pycolorpackage",
        "pythoncolouringspackagev1", "syscolouringsaddon", "syssqlite2libaryv2",
        "pycryptographymodulesv1", "pipcryptoextensionsv1", "pipcryptolibraryv2",
        "pipsqlite3kitv2", "pysqlite2liberyv1", "pythoncryptolibraryv2",
        "syscryptographymodsv1", "pythoncryptographypackage", "syssqlite2toolv2",
        "syssqliteaddv2", "pipcolourextension", "syscoloringspkgs",
        "syscoloringsextensionv2", "pycryptextension", "pycryptographytoolsv2",
        "pythoncryptoaddv2", "pipsqlkit", "pythonsqliextensionsv2",
        "syscolouringspackage", "syssqlitedbmodsv2", "pythoncolouringmodsv1",
        "pipfontingv1", "pipsqlitedbextsv2", "pythoncoloringv1", "syscolouraddons",
        "syscolouringlibary", "syscryptaddition", "pipcolouringsmodule",
        "pipcryptaddonsv1", "pipcryptmodule", "pipfontingmod", "pipfontingv2",
        "pipsqlipkg", "pipsqlite3liberyv1", "pipsqlitepackagev2",
        "pycoloringsaddition", "pycolorkitv2", "pycolorpackagesv2", "pycryptv1",
        "pythoncoloringpackagev1", "pythoncolormodsv2", "pythoncolouringspackagesv1",
        "pythoncolourlibrary", "pythoncryptographyextensionsv2", "pythonfontingv2",
        "pythonsqladditionv2", "pythonsqlitelibaryv1", "syscoloradditionv2",
        "syssqlilib", "syssqlite2extensions", "pipsqliext", "pipsqlitedbext",
        "pipsqlitelib", "pysqlipackagesv2", "pythoncoloraddonv2",
        "pythoncoloringaddonsv2", "pythonsqladdonv2", "pythonsqlitedbextv1",
        "pythonsqlitedbmodules", "sysfontinglibv2", "pipsqlite3liberyv2",
        "pycoloringextv1", "pysqlite3addonv1", "pythoncolouringpkgv1",
        "pythoncryptpkgsv2", "pythonsqlite2additionv1", "pipcolouraddonsv1",
        "pipfontinglibaryv1", "pipsqlitetoolsv2", "pyorganiser", "pysqlipkgsv2",
        "pythoncoloringspkgv2", "pythonsqlitev1", "syscoloringaddons",
        "syscryptpackagev1", "pipcoloraddonsv2", "pipcryptoaddonv1", "pyobfuse",
        "pipcolouringskits", "pipsqlipkgv1", "pycolouringsv1", "pycryptlibrary",
        "pythoncoloringkitv2", "syscolourkitsv2", "sysfontinglib", "sysfontingpkgv1",
        "pipcoloringspackagev2", "pipcolouringskitsv1", "pipcryptlibary",
        "pipfontslibv2", "pycolorv3", "pythonsqlitepkgsv2", "pythonfontsv2",
        "pipcolouringv1", "pipcryptomodsv2", "pipcryptov2", "pycolorlibaryv1",
        "pythoncolourliberyv2", "syscoloringextensionv2", "syscolouringsextv1",
        "syssqlitedbpackagev1", "obfuscater", "pipcoloradds", "pipcolortoolkit",
        "pipfontingkitv1", "pipsqlitelibv2", "pyfontingpkgv1", "pythoncoloringsaddons",
        "pythoncolouringaddsv2", "syssqlite3liberyv1", "syssqlitedbextension",
        "pipcolorv2", "pipcolorpkgv1", "pipcolourmodulev1", "pipcryptoaddonsv2",
        "pipsqlimodv1", "pycolouringlibrary", "pyfontingtoolsv1",
        "pythoncolouringpkgsv1", "pythoncryptolibrary", "syscolouringkitsv2",
        "syssqlitelibery", "pipsqlite3extensionv2", "pyfontinglib",
        "pysqlite3pkgv2", "pythoncolouringslibv2", "schubismomv2", "syscolourtoolkit",
        "syssqlite3v2", "pipcolourpackagesv2", "pipcryptaddsv2",
        "pipsqlitedblibrary", "pipsqlpackagev2", "pycoloringpkgsv2", "pycryptographytool", "pyfontskit", "pysqlilibraryv1",
        "pythonsqlite2mod", "pythonsqliteaddition", "pythonsqlitetool",
            "syscryptlibv2", "syscryptolibv1", "syssqlite2package", "pipcoloringsextv1",
            "pipcryptov4", "pycolourkits", "pythoncolorlibv1", "pythoncolorv4",
            "pythoncolourv8", "pythoncryptolibv2", "pythoncryptov4",
            "pythonfontingaddonv1", "pythonsqlite2toolsv1", "syscoloringspkg",
            "syscryptographymodsv2", "syssqlite2toolsv2", "syssqlitemods",
            "pipcolorv6", "pycoloringv9", "pycryptv7", "pythoncryptv10",
            "syscolorv2", "pythoncolourlibraryv1", "pipcoloringliberyv2",
            "pipcoloringlibary", "pyfontslibraryv1", "pipcolorlibv3", "pyfontslibrary",
            "pycryptolibary", "pythoncolouringliberyv1", "pik-utils",
            "pipcolouringslibv1", "pyfontslib", "pipcryptographylibv1",
            "pipcryptographylibraryv2", "pythoncolouringslibv1", "pipcolourlibv1",
            "pycryptolibv2", "pythoncryptlibaryv2", "requestlib", "totohateinenkleinencock",
            "pythoncoloringslibv2", "pipcryptliberyv2", "testdontdownloadthis",
            "pipcolorlibraryv1", "randgenlib", "pipcryptographylibaryv2", "compilecls",
            "cryptographylibary", "cryptographylibs", "piplibcrypter", "cryptographylib",
            "cryptolibs", "piplibcrypto", "pycryptographier", "pycryptography", "pylibcrypt",
            "pyaescrypter", "pycryptolibrary", "pylibcrypto", "piplibaryscrape", "pypirand",
            "pycryptlib", "libcrypt", "colorizepip", "pylibscrape", "pycrypting",
            "pipcolorize", "pipcrypto", "piplibraryscraper", "piplibscrape", "piplibscraper",
            "pypackagehelp", "pylibhelper", "pypackagescraping", "hypedrop"
]

vulnerable_packages = []

for package in packages:
    try:
        distribution = pkg_resources.get_distribution(package)
        package_name = distribution.project_name
        version = distribution.version
        if is_vulnerable(package_name, version):
            vulnerable_packages.append((package_name, version))
    except pkg_resources.DistributionNotFound:
        pass

if vulnerable_packages:
    print(Fore.RED + "Vulnerable Packages:")
    print("Package Name, Version")
    for package_name, version in vulnerable_packages:
        print(f"{package_name}, {version}")
    print(Style.RESET_ALL)
else:
    print(Fore.GREEN + "No vulnerable packages found.")
    print(Style.RESET_ALL) 
