import {
    withStreamlitConnection,
    StreamlitComponentBase,
} from "streamlit-component-lib"
import { ChessBoardElement } from "chessboard-element/lib/chessboard-element"

class Board extends StreamlitComponentBase {
    render() {
        const fen = this.props.args["fen"] || "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        
        return (
            <chess-board
                draggable-pieces
                position={fen}>
            </chess-board>
        )
    }
}

export default withStreamlitConnection(Board)
