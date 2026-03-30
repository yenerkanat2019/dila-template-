#!/bin/bash
# chmod +x git_push.sh

git add --all .
# git commit -m "TUR-33532: Yüklenici Sözleşmesi"
git commit -m "templates"
# git commit -m "runModuleStandardTests duzeltmeleri ve modullerin testleri"
# git commit -m "kokpitde Rendering Error : renderer null :  type, model, propertyName ORGUNIT unit undefined "
# 32736

if [ $? -ne 0 ]; then
  echo "⚠️ Commit yapılamadı (değişiklik yok veya hata var)"
  exit 1
fi

git pull --no-rebase origin

# Eğer conflict çıktıysa
if [ $? -ne 0 ]; then
  echo "⚠️ Conflict oluştu. Lütfen şunları yap:"
  echo "1. Conflictleri çöz"
  echo "2. git add <çözülen-dosyalar>"
  echo "3. git commit (merge commit için)"
  echo "4. git push origin bootstrap5dev-working"
  exit 1
fi

git push origin
# fuser -k 4000/tcp || true

# jSuites
# jspreadsheet
# git add .
# git commit -m "gitignore"
# git push origin HEAD

# conflict cikarsa cozdukden sonra
# git add --all .
# git rebase --continue
# git push origin HEAD
# git pull





# conflict cikinca
# git checkout --theirs .
# git add --all .
# git rebase --continue

# http://localhost:4000/rest/s/68d67436b1daba17c461703c

# error: failed to push some
# git pull --rebase origin TUR-30313-tahliye-plani
# # conflict olursa çözüp
# git add .
# git rebase --continue
# git push origin TUR-30313-tahliye-plani
# git sync

# git config --global alias.rebase-theirs '!f(){ while ! git rebase --continue 2>/dev/null; do git checkout --theirs . && git add .; done; }; f'
# git rebase-theirs

# git config --global alias.sync '!f(){ b=$(git rev-parse --abbrev-ref HEAD); git pull --rebase origin $b && git push origin $b; }; f'

# git config --global alias.pull-theirs '!f(){ git fetch origin && while ! git pull --rebase -X theirs; do git checkout --theirs . && git add .; done; }; f'
# git pull-theirs


# git commit --allow-empty -m "TUR-30804:Çalışan sayfasında gösterilen bir sonraki muayene tarihi sayfa yenilemesinden sonra değişiyor https://perfektive.atlassian.net/browse/TUR-30804"
# git push

# (reporter = currentUser() OR assignee=currentUser() ) AND (status CHANGED TO "Test" ) AND (statusCategory!= "To Do" AND statusCategory!= "In Progress") AND updatedDate>= "2025-06-30" order by updated DESC

# AND statusCategory != "In Progress" AND statusCategory != "To Do"
# assignee IN (5c87a9305db2976adad457fb) AND updated >= "2025-06-30" AND updated <= "2025-07-09" AND status CHANGED to "Test" ORDER BY updated DESC


# git log --since="6 days ago" --author="Yener" --pretty=format:"%h %s"

# table responsive ornegi
# tg-gipsy-ui/src/main/webapp/app/view/drct/list/limited-user-list.html


# git reset --hard
# git clean -fd
# git rebase --abort
# git fetch origin
# git reset --hard origin/dev
# git status



# branch listesini al
# git fetch origin
# git checkout TUR-31643-bootstrap3-de-duzeltmeler2


# https://worksafedemo.kocsistem.com.tr
# https://ksworksafe.kocsistem.com.tr
# worksafetest01@kocsistem.onmicrosoft.com
# >@HP"m:L&T^t?d7R



# git pull --rebase origin dev
# git add .
# git commit
# git rebase --continue
# git push origin dev
# new-entities-table

# git merge --abort
# git reset --hard HEAD
# git stash clear
# git log --oneline -5

#   TUR-28550-bootstrap5
#   TUR-29495-bootstrap3-e-bagli-olmayan-kut
# * TUR-29509-grafik-olarak-highchart-ve-ant
#   dev
#   master

# git reset --hard ee37401c4c
# git push origin bootstrap5dev --force
# git log --oneline -5

# meeting
# blueprint
# metric
# ibys
# timeline
# examination-policlinic
# drill
# checklist-spec
# hse-prescription
# subcontractor-employee
# stock-item
