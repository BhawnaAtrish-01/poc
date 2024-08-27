from django.urls import path
from .views import ExcelUploadView
from .views import ExcelDataView
from .views import (
    ModifyRecordView,
    AddColumnView,
    SoftDeleteColumnView,
    RenameColumnView,
    ExcelExportView,
    PdfExportView,
    ColDeletionApprovedView,
    ColDeletionRejectedView,
    RecordDeletionApproved,
    RecordDeletionDisapproved,
)

urlpatterns = [
    path("upload/", ExcelUploadView.as_view(), name="excel-upload"),
    path("data/", ExcelDataView.as_view(), name="excel-data"),
    path("create_or_update_record/", ModifyRecordView.as_view(), name="create-record"),
    path(
        "create_or_update_record/<str:record_id>/",
        ModifyRecordView.as_view(),
        name="update-record",
    ),
    path("add-column/", AddColumnView.as_view(), name="add_column"),
    path(
        "soft-delete-column/", SoftDeleteColumnView.as_view(), name="soft_delete_column"
    ),
    path("rename-column/", RenameColumnView.as_view(), name="rename_column"),
    path("export/excel/", ExcelExportView.as_view(), name="export_excel"),
    path("export/pdf/", PdfExportView.as_view(), name="export_pdf"),
    path(
        "col_deletion_approval/<str:record_id>/",
        ColDeletionApprovedView.as_view(),
        name="col_deletion_approval",
    ),
    path(
        "col_deletion_rejection/<str:record_id>/",
        ColDeletionRejectedView.as_view(),
        name="col_deletion_rejection",
    ),
    path(
        "record_deletion_approved/<str:record_id>/",
        RecordDeletionApproved.as_view(),
        name="record_deletion_approved",
    ),
    path(
        "record_deletion_disapproved/<str:record_id>/",
        RecordDeletionDisapproved.as_view(),
        name="record_deletion_disapproved",
    ),
]
