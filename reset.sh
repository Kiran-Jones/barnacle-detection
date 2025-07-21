#!/usr/bin/env bash
# reset.sh: clears all frames and results generated 

OUTPUT_DIR="outputs"
FRAME_DIR="frames"
PLOTS_DIR="plots"



echo "Resetting all pipeline outputs…"

if [[ -d $OUTPUT_DIR ]]; then
  rm -rf "${OUTPUT_DIR:?}/"* # ensure that OUTPUT_DIR is not empty i.e. cannot delete *
  echo "Cleared $OUTPUT_DIR"
else
  echo "$OUTPUT_DIR does not exist"
fi

if [[ -n "$FRAME_DIR" && -d $FRAME_DIR ]]; then
  rm -rf "${FRAME_DIR:?}/"*
  echo "Cleared $FRAME_DIR"
else
  echo "$FRAME_DIR does not exist or is unset"
fi

if [[ -d $PLOTS_DIR ]]; then
  rm -rf "${PLOTS_DIR:?}/"* 
  echo "Cleared $PLOTS_DIR"
else
  echo "$PLOTS_DIR does not exist"
fi


echo "Done."