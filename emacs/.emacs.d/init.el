;; These config will be restored to the default values after-init-hook
;; https://www.reddit.com/r/emacs/comments/3kqt6e/2_easy_little_known_steps_to_speed_up_emacs_start/

;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(defvar file-name-handler-alist-old file-name-handler-alist)
(setq file-name-handler-alist nil)
(setq gc-cons-threshold 402653184)
(setq gc-cons-percentage 0.6)

;; Restore to the default values.
(add-hook 'after-init-hook
          `(lambda ()
             (setq file-name-handler-alist file-name-handler-alist-old)
             (setq gc-cons-threshold 800000)
             (setq gc-cons-percentage 0.1)))

(add-to-list 'load-path (expand-file-name "init.d" user-emacs-directory))
(setq custom-file (expand-file-name "custom.el" user-emacs-directory))

(global-unset-key (kbd "C-q"))

(require 'init-functions)
(require 'init-general)
(require 'init-packages)
(require 'init-local)

(if (eq system-type 'windows-nt)
    (require 'init-windows)
  (require 'init-nix))

(provide 'init)
