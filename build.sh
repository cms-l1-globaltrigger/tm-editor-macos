set -e

UTM_VERSION=0.11.2
TME_VERSION=0.15.3

export MACOSX_DEPLOYMENT_TARGET=10.15

BUILD_DIR=build
ENV_NAME=env

# Install system dependencies
brew install gcc boost swig xerces-c

# Create build area
rm -rf $BUILD_DIR
mkdir -p $BUILD_DIR
cd $BUILD_DIR

python3.11 -m venv $ENV_NAME
. $ENV_NAME/bin/activate

# Install dependencies
pip install -U pip
pip install -r ../requirements.txt

# Build utm
git clone https://gitlab.cern.ch/cms-l1t-utm/utm.git
cd utm
git checkout utm_${UTM_VERSION}
./configure
make -j8 all SUBDIRS='tmUtil tmXsd tmTable tmGrammar' CPPFLAGS='-DNDEBUG -DSWIG'  # compile with -DSWIG
. ./env.sh
cd ..

# Build tm-grammar
git clone https://github.com/cms-l1-globaltrigger/tm-grammar.git
cd tm-grammar
git checkout ${UTM_VERSION}
pip install .
cd ..

# Build tm-table
git clone https://github.com/cms-l1-globaltrigger/tm-table.git
cd tm-table
git checkout ${UTM_VERSION}
pip install .
cd ..

# Build tm-editor
git clone https://github.com/cms-l1-globaltrigger/tm-editor.git
cd tm-editor
git checkout ${TME_VERSION}
pyrcc5 resource/tmEditor.rcc -o tmEditor/tmeditor_rc.py
pip install . --no-deps
cd ..

# Build app
cd ..
pyinstaller macos.spec

echo "Done."
