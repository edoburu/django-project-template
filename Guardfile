# A sample Guardfile
# More info at https://github.com/guard/guard#readme
#
# Installation requirements:
#
#   gem install guard-livereload guard-compass
#
# Browser plugins:
#   All: http://help.livereload.com/kb/general-use/browser-extensions
#   Firefox (2.0.9 dev release): https://github.com/siasia/livereload-extensions/downloads
#
notification :off
interactor :off
logger :level => :info

guard 'compass' do
  # Always touch screen.scss too, a workaround for compass 0.12.2
  watch(%r{(.*)\.s[ac]ss$}) {|m| "frontend/sass/screen.scss"}
end

guard 'livereload', :host => '127.0.0.1' do
  watch(%r{.+\.(css|js|html)$})
  #watch(%r{.+\.(css|js|html|pyc)$})
end
