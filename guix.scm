;; evtest-qt - A graphical joystick tester
;; Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

(set! %load-path
  (cons* "/ipfs/QmcQaosGtaQ6dsb4iykNihZ2ZTie8om2i7pgHucZ9Ranyq/guix-cocfree_0.0.0-64-gd618440"
         %load-path))

(use-modules (guix packages)
             (guix build utils)
             (guix build-system cmake)
             ((guix licenses) #:prefix license:)
             (gnu packages qt)
             (guix-cocfree utils))

(define %source-dir (dirname (current-filename)))

(define-public evtest-qt
  (package
   (name "evtest-qt")
   (version (version-from-source %source-dir))
   (source (source-from-source %source-dir #:version version))
   (build-system cmake-build-system)
   (arguments
    `(#:tests? #f))
   (inputs
    `(("qtbase" ,qtbase-5)
      ))
   (synopsis (synopsis-from-source %source-dir))
   (description (description-from-source %source-dir))
   (home-page (homepage-from-source %source-dir))
   (license license:gpl3+)))

evtest-qt

;; EOF ;;
