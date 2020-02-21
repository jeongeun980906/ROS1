
(cl:in-package :asdf)

(defsystem "project_practice_1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "project_practice1" :depends-on ("_package_project_practice1"))
    (:file "_package_project_practice1" :depends-on ("_package"))
  ))