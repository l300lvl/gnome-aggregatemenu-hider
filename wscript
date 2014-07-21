#! /usr/bin/env python

from csv import DictReader

def options(ctx):
  configure(ctx)

def configure(ctx):
  ctx.load('template', tooldir='.')
  ctx.load('gnu_dirs')

def build(ctx):
  with open('extensions.csv') as f:
    for extension in DictReader(f):
      name = extension['name']
      shortname = name.partition(' ')[0]
      uuid = 'hide-' + shortname + '@' + extension['author']
      ctx(source='extension.js.in metadata.json.in',
          mapping={
            'name': name,
            'uuid': uuid,
            'item': extension['item'],
            'description': extension['description']},
          name=shortname,
          out_dir=uuid,
          install_path='${DATAROOTDIR}/gnome-shell/extensions/' + uuid)
