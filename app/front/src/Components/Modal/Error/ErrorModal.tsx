import {
  Button,
  Card,
  CardActions,
  CardContent,
  Modal,
  Typography,
} from "@material-ui/core";
import React from "react";
import "./ErrorModal.scss";

export function ErrorModal({ open, close, error }: any) {
  return (
    <Modal
      className="modal"
      open={open}
      onClose={close}
      aria-labelledby="simple-modal-title"
      aria-describedby="simple-modal-description"
    >
      <Card className="card-modal">
        <CardContent>
          <Typography variant="h3" component="h2" color="secondary">
            {error?.code}404
          </Typography>
          <img src="/error.svg" alt="" />
        </CardContent>
        <CardActions>
          <Button variant="contained" color="primary" onClick={close}>
            OK
          </Button>
        </CardActions>
      </Card>
    </Modal>
  );
}
