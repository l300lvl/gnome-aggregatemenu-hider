# Maintainer: XZS <d.f.fischer at web dot de>

# To only build some of the extensions, remove
# the unwanted ones from the $extensions variable.
extensions=('brightness' 'volume' 'user' 'location')
pkgbase='gnome-shell-extension-aggregatemenu-hider'
for e in ${extensions[@]}; do
  local pkg=gnome-shell-extension-hide-$e
  pkgname+=($pkg)
  eval "package_${pkg}() {
    package ${e^*}
  }"
done

pkgver=1
pkgrel=1
arch=(any)
url='https://github.com/dffischer/gnome-aggregatemenu-hider'
license=(GPLv3)
depends=('gnome-shell')
makedepends=('waf')
source=("$pkgbase::git://github.com/dffischer/gnome-aggregatemenu-hider.git")
md5sums=('SKIP')

build() {
  join() {
    local IFS="$1"; shift; echo "$*";
  }
  cd $pkgbase
  waf --prefix=/usr configure
  waf --targets=$(join , ${extensions[@]^*}) build
}

package() {
  cd $pkgbase
  waf --destdir="$pkgdir" --targets=$1 install
}

