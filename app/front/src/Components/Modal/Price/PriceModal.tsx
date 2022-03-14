import React from "react";
import {
  Button,
  Card,
  CardActions,
  CardContent,
  InputAdornment,
  Modal,
  TextField,
  Typography,
} from "@material-ui/core";
import { AttachMoney } from "@material-ui/icons";

export function PriceModal({
  open,
  close,
  price,
  setPrice,
  sendRealValue,
}: any) {
  return (
    <Modal
      className="modal"
      open={open}
      onClose={close}
      aria-labelledby="simple-modal-title"
      aria-describedby="simple-modal-description"
    >
      <Card>
        <CardContent>
          <Typography variant="h5" component="h2">
            Price
          </Typography>
          <TextField
            id="price-input"
            name="price"
            label="Price"
            required
            variant="filled"
            color="secondary"
            type="number"
            value={price}
            onChange={(event: any) => setPrice(event.target.value)}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <AttachMoney />
                </InputAdornment>
              ),
            }}
          />
        </CardContent>
        <CardActions>
          <Button variant="contained" color="primary" onClick={sendRealValue}>
            OK
          </Button>
        </CardActions>
      </Card>
    </Modal>
  );
}
