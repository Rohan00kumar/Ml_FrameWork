def custom_metric(y_true, y_pred):
    # Example custom metric
    return tf.reduce_mean(tf.cast(tf.equal(tf.round(y_pred), y_true), tf.float32))
