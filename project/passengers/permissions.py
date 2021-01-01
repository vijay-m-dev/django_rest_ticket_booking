from rest_framework import permissions

'''class IsOwner(permissions.BasePermission):
	message="You must be the owner of the object"
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user'''

class IsOwnerOrAdmin(permissions.BasePermission):
	message="You must be the owner or admin of the object"
	def has_object_permission(self, request, view, obj):
		return obj.booking.user == request.user or request.user.is_superuser