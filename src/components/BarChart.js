import React, { useState } from "react";

import { VictoryBar } from "victory";

const styles = {
  container: {
    backgroundColor: "#ccc",
    borderRadius: 3,
    width: 500,
    height: 500,
    padding: 4,
    margin: 8
  },
}

const sampleData = [
  { x: 1, y: 2, y0: 1 },
  { x: 2, y: 3, y0: 2 },
  { x: 3, y: 5, y0: 2 },
  { x: 4, y: 4, y0: 3 },
  { x: 5, y: 6, y0: 3 }
];

const sampleData2 = [
  { x: 1, y: 2, y0: 1 },
  { x: 2, y: 3, y0: 2 },
  { x: 3, y: 5, y0: 2 },
  { x: 4, y: 4, y0: 3 },
  { x: 5, y: 6, y0: 3 },
  { x: 6, y: 3, y0: 4 },
];

const BarChart = () => {

  const [dataIdx, setDataIdx] = useState(0);

  const onClickHandle = () => {
    setDataIdx(1);
  }

  // const currentData = {(dataIdx === 1)? sampleData : sampleData2}

  return (
    <div style={styles.container}>
      <VictoryBar
        animate={{
          duration: 2000,
          onLoad: { duration: 1000 }
        }}
        style={{
          data: { fill: "#c43a31" }
        }}
        onClick={onClickHandle}
        events={[{
          target: "data",
          eventHandlers: {
            onClick: () => {
              onClickHandle();
              return [
                {
                  target: "data",
                  mutation: (props) => {
                    const fill = props.style && props.style.fill;
                    return fill === "black" ? null : { style: { fill: "black" } };
                  }
                }
              ];
            }
          }
        }]}
        data={(dataIdx === 0)? sampleData : sampleData2}
      />
    </div>
  );
}
    
export default BarChart;