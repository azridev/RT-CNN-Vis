import tensorflow as tf

def gradCam(y,A):
    """
    y,A according to paper
    """
    y = tf.reduce_max(y,axis=-1)[0]
    mapImportanceGradients = tf.gradients(y,A)
    importanceWeights = tf.reduce_mean(mapImportanceGradients, axis=[2,3],keepdims=True)
    # shape extended with one in beginning?
    weightsReshaped = importanceWeights[0]
    weightedFeatureMap = weightsReshaped*A
    gradCamRes = tf.reduce_mean(weightedFeatureMap,axis=[-1])[0]
    # x / (K.sqrt(K.mean(K.square(x))) + 1e-5)
    # gradCamRes = gradCamRes/ tf.sqrt(tf.mean(tf.square(gradCamRes))+1e-5)
    return gradCamRes