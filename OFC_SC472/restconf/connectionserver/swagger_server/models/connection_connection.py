# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.topology_layer_protocol_name import TopologyLayerProtocolName  # noqa: F401,E501
from swagger_server import util


class ConnectionConnection(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, target_port: str=None, source_port: str=None, target_node: str=None, connection_id: str=None, bandwidth: int=None, source_node: str=None, layer_protocol_name: TopologyLayerProtocolName=None):  # noqa: E501
        """ConnectionConnection - a model defined in Swagger

        :param target_port: The target_port of this ConnectionConnection.  # noqa: E501
        :type target_port: str
        :param source_port: The source_port of this ConnectionConnection.  # noqa: E501
        :type source_port: str
        :param target_node: The target_node of this ConnectionConnection.  # noqa: E501
        :type target_node: str
        :param connection_id: The connection_id of this ConnectionConnection.  # noqa: E501
        :type connection_id: str
        :param bandwidth: The bandwidth of this ConnectionConnection.  # noqa: E501
        :type bandwidth: int
        :param source_node: The source_node of this ConnectionConnection.  # noqa: E501
        :type source_node: str
        :param layer_protocol_name: The layer_protocol_name of this ConnectionConnection.  # noqa: E501
        :type layer_protocol_name: TopologyLayerProtocolName
        """
        self.swagger_types = {
            'target_port': str,
            'source_port': str,
            'target_node': str,
            'connection_id': str,
            'bandwidth': int,
            'source_node': str,
            'layer_protocol_name': TopologyLayerProtocolName
        }

        self.attribute_map = {
            'target_port': 'target-port',
            'source_port': 'source-port',
            'target_node': 'target-node',
            'connection_id': 'connection-id',
            'bandwidth': 'bandwidth',
            'source_node': 'source-node',
            'layer_protocol_name': 'layer-protocol-name'
        }
        self._target_port = target_port
        self._source_port = source_port
        self._target_node = target_node
        self._connection_id = connection_id
        self._bandwidth = bandwidth
        self._source_node = source_node
        self._layer_protocol_name = layer_protocol_name

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectionConnection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The connection.Connection of this ConnectionConnection.  # noqa: E501
        :rtype: ConnectionConnection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_port(self) -> str:
        """Gets the target_port of this ConnectionConnection.


        :return: The target_port of this ConnectionConnection.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port: str):
        """Sets the target_port of this ConnectionConnection.


        :param target_port: The target_port of this ConnectionConnection.
        :type target_port: str
        """

        self._target_port = target_port

    @property
    def source_port(self) -> str:
        """Gets the source_port of this ConnectionConnection.


        :return: The source_port of this ConnectionConnection.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port: str):
        """Sets the source_port of this ConnectionConnection.


        :param source_port: The source_port of this ConnectionConnection.
        :type source_port: str
        """

        self._source_port = source_port

    @property
    def target_node(self) -> str:
        """Gets the target_node of this ConnectionConnection.


        :return: The target_node of this ConnectionConnection.
        :rtype: str
        """
        return self._target_node

    @target_node.setter
    def target_node(self, target_node: str):
        """Sets the target_node of this ConnectionConnection.


        :param target_node: The target_node of this ConnectionConnection.
        :type target_node: str
        """

        self._target_node = target_node

    @property
    def connection_id(self) -> str:
        """Gets the connection_id of this ConnectionConnection.


        :return: The connection_id of this ConnectionConnection.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id: str):
        """Sets the connection_id of this ConnectionConnection.


        :param connection_id: The connection_id of this ConnectionConnection.
        :type connection_id: str
        """

        self._connection_id = connection_id

    @property
    def bandwidth(self) -> int:
        """Gets the bandwidth of this ConnectionConnection.


        :return: The bandwidth of this ConnectionConnection.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth: int):
        """Sets the bandwidth of this ConnectionConnection.


        :param bandwidth: The bandwidth of this ConnectionConnection.
        :type bandwidth: int
        """

        self._bandwidth = bandwidth

    @property
    def source_node(self) -> str:
        """Gets the source_node of this ConnectionConnection.


        :return: The source_node of this ConnectionConnection.
        :rtype: str
        """
        return self._source_node

    @source_node.setter
    def source_node(self, source_node: str):
        """Sets the source_node of this ConnectionConnection.


        :param source_node: The source_node of this ConnectionConnection.
        :type source_node: str
        """

        self._source_node = source_node

    @property
    def layer_protocol_name(self) -> TopologyLayerProtocolName:
        """Gets the layer_protocol_name of this ConnectionConnection.


        :return: The layer_protocol_name of this ConnectionConnection.
        :rtype: TopologyLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: TopologyLayerProtocolName):
        """Sets the layer_protocol_name of this ConnectionConnection.


        :param layer_protocol_name: The layer_protocol_name of this ConnectionConnection.
        :type layer_protocol_name: TopologyLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name
